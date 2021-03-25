// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton, ImageField, BooleanField } from 'react-admin';

export const CovenantList: FC = (props) => (
  <List {...props} title="Listar convênios">
    <Datagrid>
      <ImageField title="Logo" source="logo_file" />
      <TextField label="Nome convênio" source="name" />
      <TextField label="Iniciais" source="initials" />
      <BooleanField label="Finalizado?" source="finished" />
      <EditButton />
    </Datagrid>
  </List>
);
