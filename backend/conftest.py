import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from fastapi.testclient import TestClient
import typing as t

from app.core import config, security
from app.db.session import Base, get_db
from app.db import models
from app.main import app


def get_test_db_url() -> str:
    return f"{config.SQLALCHEMY_DATABASE_URI}_test"

@pytest.fixture
def test_db():
    """
    Modify the db session to automatically roll back after each test.
    This is to avoid tests affecting the database state of other tests.
    """
    # Connect to the test database
    engine = create_engine(
        get_test_db_url(),
    )

    connection = engine.connect()
    trans = connection.begin()

    # Run a parent transaction that can roll back all changes
    test_session_maker = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    test_session = test_session_maker()
    test_session.begin_nested()

    @event.listens_for(test_session, "after_transaction_end")
    def restart_savepoint(s, transaction):
        if transaction.nested and not transaction._parent.nested:
            s.expire_all()
            s.begin_nested()

    yield test_session

    # Roll back the parent transaction after the test is complete
    test_session.close()
    trans.rollback()
    connection.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    """
    Create a test database and use it for the whole test session.
    """

    test_db_url = get_test_db_url()

    # Create the test database
    assert not database_exists(
        test_db_url
    ), "Test database already exists. Aborting tests."
    create_database(test_db_url)
    test_engine = create_engine(test_db_url)
    Base.metadata.create_all(test_engine)

    # Run the tests
    yield

    # Drop the test database
    drop_database(test_db_url)


@pytest.fixture
def client(test_db):
    """
    Get a TestClient instance that reads/write to the test database.
    """

    def get_test_db():
        yield test_db

    app.dependency_overrides[get_db] = get_test_db

    yield TestClient(app)


@pytest.fixture
def test_password() -> str:
    return "securepassword"


def get_password_hash() -> str:
    """
    Password hashing can be expensive so a mock will be much faster
    """
    return "supersecrethash"


@pytest.fixture
def test_pg(test_db) -> models.PostGraduation:
    """
    Make a test postgraduation in the database
    """

    pg = models.PostGraduation(
        id_unit=5679,
        name="Gestão Pública",
        initials="PPGP",
        sigaa_code="1672",
        is_signed_in=True,
        old_url="",
        description_small="",
        description_big="",
    )
    test_db.add(pg)
    test_db.commit()
    return pg

@pytest.fixture
def test_user(test_db, test_pg) -> models.User:
    """
    Make a test user in the database
    """

    user = models.User(
        email="fake@email.com",
        owner_id=test_pg.id,
        hashed_password=get_password_hash(),
        is_active=True,
    )
    test_db.add(user)
    test_db.commit()
    return user

@pytest.fixture
def test_superuser(test_db, test_pg) -> models.User:
    """
    Superuser for testing
    """

    user = models.User(
        email="fakeadmin@email.com",
        owner_id=test_pg.id,
        hashed_password=get_password_hash(),
        is_superuser=True,
    )
    test_db.add(user)
    test_db.commit()
    return user


def verify_password_mock(first: str, second: str) -> bool:
    return True


@pytest.fixture
def user_token_headers(
        client: TestClient, test_user, test_password, monkeypatch
) -> t.Dict[str, str]:
    monkeypatch.setattr(security, "verify_password", verify_password_mock)

    login_data = {
        "username": test_user.email,
        "password": test_password,
    }
    r = client.post("/api/token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


@pytest.fixture
def superuser_token_headers(
        client: TestClient, test_superuser, test_password, monkeypatch
) -> t.Dict[str, str]:
    monkeypatch.setattr(security, "verify_password", verify_password_mock)

    login_data = {
        "username": test_superuser.email,
        "password": test_password,
    }
    r = client.post("/api/token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers

@pytest.fixture
def test_course(test_db, test_pg) -> models.Course:
    """
    Course for testing
    """
    course = models.Course(
        owner_id=test_pg.id,
        name="Musica",
        id_sigaa=84798578,
        course_type=models.CourseType.masters
    )
    test_db.add(course)
    test_db.commit()
    return course

@pytest.fixture
def test_researcher(test_db, test_pg) -> models.Researcher:
    """
    Researcher for testing
    """
    researcher = models.Researcher(
        owner_id=test_pg.id,
        name="Maria Arlete",
        cpf="12345678910"
    )
    test_db.add(researcher)
    test_db.commit()
    return researcher

@pytest.fixture
def test_covenant(test_db, test_pg) -> models.Covenant:
    """
    covenant for testing
    """
    covenant = models.Covenant(
        owner_id=test_pg.id,
        name="Covenant test",
        logo_file="dummy.pdf",
        initials="CT"
    )
    test_db.add(covenant)
    test_db.commit()
    return covenant

@pytest.fixture
def test_official_document(test_db, test_pg) -> models.OfficialDocument:
    """
    official document for testing
    """
    official_document = models.OfficialDocument(
        owner_id=test_pg.id,
        title="Official document test",
        file="dummy.pdf",
        cod="CT",
        category="regiments"
    )
    test_db.add(official_document)
    test_db.commit()
    return official_document

@pytest.fixture
def test_participation(test_db, test_pg) -> models.Participation:
    """
    participation for testing
    """
    participation = models.Participation(
        owner_id=test_pg.id,
        title="Teste",
        description="Teste",
        year=2020,
        international=False,
    )
    test_db.add(participation)
    test_db.commit()
    return participation

@pytest.fixture
def test_event(test_db, test_pg) -> models.Event:
    """
    event for testing
    """
    event = models.Event(
        owner_id=test_pg.id,
        title="Teste",
        link="https://google.com.br",
        initial_date="2021-02-20",
        final_date="2021-02-21",
    )
    test_db.add(event)
    test_db.commit()
    return event

@pytest.fixture
def test_scheduled_report(test_db, test_pg) -> models.ScheduledReport:
    """
    scheduled report for testing
    """
    scheduled_report = models.ScheduledReport(
        owner_id=test_pg.id,
        title="Teste",
        author="Luccas",
        location="Nepsa 2",
        datetime="2021-02-20T15:31:19.739000+00:00",
    )
    test_db.add(scheduled_report)
    test_db.commit()
    return scheduled_report

@pytest.fixture
def test_news(test_db, test_pg) -> models.News:
    """
    news for testing
    """
    news = models.News(
        owner_id=test_pg.id,
        title="Teste",
        headline="Headline test",
        date="2021-02-20",
        body="""Sed ut perspiciatis unde omnis iste natus error sit
        voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quae ab illo inventore veritatis et quasi architecto
        beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni
        dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est,
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat
        voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis"""
    )
    test_db.add(news)
    test_db.commit()
    return news

@pytest.fixture
def test_attendance(test_db, test_pg) -> models.Attendance:
    """
    attendance for testing
    """
    attendance = models.Attendance(
        owner_id=test_pg.id,
        email="test@email.com",
        location="Rua e tals",
        schedule="Dia todo"
    )
    test_db.add(attendance)
    test_db.commit()
    test_db.refresh(attendance)
    return attendance
