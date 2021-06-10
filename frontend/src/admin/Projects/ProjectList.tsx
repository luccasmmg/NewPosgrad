// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  SelectField,
  EditButton,
} from 'react-admin';

export const ProjectList: FC = (props) => (
  <List {...props} title="Listar projetos">
    <Datagrid>
      <TextField source="id" />
      <TextField label="Nome" source="name" />
      <TextField label="Email" source="email" />
      <TextField label="Situação" source="status" />
      <TextField label="Ano" source="year" />
      <TextField label="Coordenador" source="coordinator_data.name" />
      <EditButton />
    </Datagrid>
  </List>
);
