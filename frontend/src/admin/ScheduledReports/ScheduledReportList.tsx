// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, DateField, EditButton } from 'react-admin';

export const ScheduledReportList: FC = (props) => (
  <List {...props} title="Listar defesas">
    <Datagrid>
      <TextField source="id" />
      <TextField label="Titulo" source="title" />
      <TextField label="Autor" source="author" />
      <TextField label="Localização" source="location" />
      <DateField showTime label="Data - Horário" source="datetime" />
      <EditButton />
    </Datagrid>
  </List>
);
