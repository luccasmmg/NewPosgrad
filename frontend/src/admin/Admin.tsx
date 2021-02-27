import React, { FC } from 'react';
import { fetchUtils, Admin as ReactAdmin, Resource } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import authProvider from './authProvider';

import { UserList, UserEdit, UserCreate } from './Users';
import { CourseList, CourseEdit, CourseCreate } from './Courses';
import {
  PosGraduationList,
  PosGraduationCreate,
  PosGraduationEdit,
} from './PosGraduations';

const httpClient = (url: any, options: any) => {
  if (!options) {
    options = {};
  }
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider('api/v1', httpClient);

export const Admin: FC = () => {
  return (
    <ReactAdmin dataProvider={dataProvider} authProvider={authProvider}>
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
      ]}
    </ReactAdmin>
  );
};
