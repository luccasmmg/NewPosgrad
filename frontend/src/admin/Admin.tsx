import React, { FC } from 'react';
import { Admin as ReactAdmin, Resource } from 'react-admin';
import myDataProvider from './myDataProvider';
import authProvider from './authProvider';

import { UserList, UserEdit, UserCreate } from './Users';
import { CovenantCreate, CovenantList, CovenantEdit } from './Covenants';
import { StaffCreate, StaffList, StaffEdit } from './Staff';
import { NewsList, NewsEdit, NewsCreate } from './News';
import { EventList, EventEdit, EventCreate } from './Events';
import {
  ParticipationList,
  ParticipationEdit,
  ParticipationCreate,
} from './Participations';
import {
  StudentAdvisorList,
  StudentAdvisorEdit,
  StudentAdvisorCreate,
} from './StudentAdvisors';
import { AttendanceList, AttendanceEdit } from './Attendance';
import { CourseList, CourseEdit, CourseCreate } from './Courses';
import {
  ScheduledReportList,
  ScheduledReportEdit,
  ScheduledReportCreate,
} from './ScheduledReports';
import { PhoneList, PhoneEdit, PhoneCreate } from './Phones';
import {
  ResearcherList,
  ResearcherEdit,
  ResearcherCreate,
} from './Researchers';
import {
  PosGraduationList,
  PosGraduationCreate,
  PosGraduationEdit,
} from './PosGraduations';

export const Admin: FC = () => {
  return (
    <ReactAdmin dataProvider={myDataProvider} authProvider={authProvider}>
      {(permissions: 'admin' | 'user') => [
        permissions === 'admin' ? (
          <Resource
            name="users"
            list={UserList}
            edit={UserEdit}
            create={UserCreate}
          />
        ) : null,
        permissions === 'admin' ? (
          <Resource
            name="posgraduacao"
            options={{ label: 'Pos Graduações' }}
            list={PosGraduationList}
            create={PosGraduationCreate}
            edit={PosGraduationEdit}
          />
        ) : null,
        permissions === 'admin' ? (
          <Resource
            name="curso"
            options={{ label: 'Cursos' }}
            list={CourseList}
            create={CourseCreate}
            edit={CourseEdit}
          />
        ) : null,
        <Resource
          name="pesquisador"
          options={{ label: 'Pesquisadores' }}
          list={ResearcherList}
          create={ResearcherCreate}
          edit={ResearcherEdit}
        />,
        <Resource
          name="contato"
          options={{ label: 'Contato' }}
          list={AttendanceList}
          edit={AttendanceEdit}
        />,
        <Resource
          name="coordenador"
          options={{ label: 'Orientadores' }}
          list={StudentAdvisorList}
          edit={StudentAdvisorEdit}
          create={StudentAdvisorCreate}
        />,
        <Resource
          name="participacao"
          options={{ label: 'Participações' }}
          list={ParticipationList}
          edit={ParticipationEdit}
          create={ParticipationCreate}
        />,
        <Resource
          name="telefone"
          options={{ label: 'Telefones' }}
          list={PhoneList}
          edit={PhoneEdit}
          create={PhoneCreate}
        />,
        <Resource
          name="evento"
          options={{ label: 'Eventos' }}
          list={EventList}
          edit={EventEdit}
          create={EventCreate}
        />,
        <Resource
          name="defesa"
          options={{ label: 'Defesas' }}
          list={ScheduledReportList}
          edit={ScheduledReportEdit}
          create={ScheduledReportCreate}
        />,
        <Resource
          name="noticia"
          options={{ label: 'Noticias' }}
          list={NewsList}
          edit={NewsEdit}
          create={NewsCreate}
        />,
        <Resource
          name="convenio"
          options={{ label: 'Convênios' }}
          create={CovenantCreate}
          list={CovenantList}
          edit={CovenantEdit}
        />,
        <Resource
          name="equipe"
          options={{ label: 'Equipe' }}
          create={StaffCreate}
          list={StaffList}
          edit={StaffEdit}
        />,
      ]}
    </ReactAdmin>
  );
};
