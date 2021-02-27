// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const ResearcherList: FC = (props) => (
  <List {...props} title="Listar Pesquisadores">
    <Datagrid>
      <TextField source="id" />
      <TextField label="CPF" source="cpf" />
      <TextField label="Nome" source="name" />
      <EditButton />
    </Datagrid>
  </List>
);
