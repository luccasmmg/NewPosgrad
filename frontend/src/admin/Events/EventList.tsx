// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, DateField, EditButton } from 'react-admin';

export const EventList: FC = (props) => (
  <List {...props} title="Listar eventos">
    <Datagrid>
      <TextField source="id" />
      <TextField label="Titulo" source="title" />
      <TextField label="Link" source="link" />
      <DateField
        showTime
        type="datetime"
        label="Data inicial"
        source="initial_date"
      />
      <DateField
        showTime
        type="datetime"
        label="Data final"
        source="final_date"
      />
      <EditButton />
    </Datagrid>
  </List>
);
