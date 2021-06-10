// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  ReferenceField,
} from 'react-admin';

export const ProjectMemberList: FC = (props) => (
  <List {...props} title="Listar membros de projetos">
    <Datagrid>
      <TextField source="id" />
      <TextField label="Nome" source="name" />
      <TextField label="Cargo" source="job_title" />
      <ReferenceField label="Projeto" source="project" reference="projeto">
        <TextField source="name" />
      </ReferenceField>
      <EditButton />
    </Datagrid>
  </List>
);
