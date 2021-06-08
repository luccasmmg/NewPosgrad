// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, DateField, EditButton } from 'react-admin';

interface Props {
  id?: any;
  record?: any;
  resource?: any;
}

const PostPanel: FC<Props> = ({ id, record, resource }) => (
  <div dangerouslySetInnerHTML={{ __html: record.body }} />
);

export const ImpactList: FC = (props) => (
  <List
    {...props}
    title="Listar impactos - O mais recente será mostrado na pagina pública"
  >
    <Datagrid expand={<PostPanel />}>
      <TextField source="id" />
      <DateField label="Data" source="inserted_on" />
      <EditButton />
    </Datagrid>
  </List>
);
