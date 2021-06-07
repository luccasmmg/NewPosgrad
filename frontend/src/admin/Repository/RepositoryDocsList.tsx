// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  NumberField,
  EditButton,
} from 'react-admin';

export const RepositoryDocsList: FC = (props) => (
  <List {...props} title="Listar documentos">
    <Datagrid>
      <TextField source="id" />
      <TextField label="Titulo" source="title" />
      <TextField label="Link" source="link" />
      <TextField label="Autor" source="author" />
      <TextField label="Ano" source="year" />
      <EditButton />
    </Datagrid>
  </List>
);
