// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton, ImageField } from 'react-admin';

export const CovenantList: FC = (props) => (
  <List {...props} title="Listar convênios">
    <Datagrid>
      <ImageField title="Logo" source="logo_file" />
      <TextField label="Nome convênio" source="name" />
      <TextField label="Iniciais" source="initials" />
      <EditButton />
    </Datagrid>
  </List>
);
