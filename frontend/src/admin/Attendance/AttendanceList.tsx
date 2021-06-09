// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton } from 'react-admin';

interface Props {
  id?: any;
  record?: any;
  resource?: any;
}

const AboutPanel: FC<Props> = ({ id, record, resource }) => (
  <div dangerouslySetInnerHTML={{ __html: record.about }} />
);

export const AttendanceList: FC = (props) => (
  <List {...props} bulkActionButtons={false} title="Contato">
    <Datagrid expand={<AboutPanel />}>
      <TextField type="email" label="Email" source="email" />
      <TextField label="Localização" source="location" />
      <TextField label="Horários" source="schedule" />
      <EditButton />
    </Datagrid>
  </List>
);
