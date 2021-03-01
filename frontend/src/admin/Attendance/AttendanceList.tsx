// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const AttendanceList: FC = (props) => (
  <List {...props} bulkActionButtons={false} title="Contato">
    <Datagrid>
      <TextField type="email" label="Email" source="email" />
      <TextField label="Localização" source="location" />
      <TextField label="Horários" source="schedule" />
      <EditButton />
    </Datagrid>
  </List>
);
