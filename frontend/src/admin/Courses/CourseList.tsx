// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const CourseList: FC = (props) => (
  <List {...props} title="Listar Cursos">
    <Datagrid>
      <TextField source="id" />
      <TextField label="ID da Pós" source="owner_id" />
      <TextField label="Nome" source="name" />
      <TextField label="Id no Sigaa" source="id_sigaa" />
      <TextField
        type="url"
        label="URL no Repositório Institucional"
        source="institutional_repository_url"
      />
      <TextField label="Type de Curso" source="course_type" />
      <EditButton />
    </Datagrid>
  </List>
);
