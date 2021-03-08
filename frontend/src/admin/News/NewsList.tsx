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

export const NewsList: FC = (props) => (
  <List {...props} title="Listar notícias">
    <Datagrid expand={<PostPanel />}>
      <TextField source="id" />
      <TextField label="Titulo" source="title" />
      <TextField label="Subtítulo" source="headline" />
      <TextField label="Data" source="date" />
      <EditButton />
    </Datagrid>
  </List>
);
