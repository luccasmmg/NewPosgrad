// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  ImageField,
  BooleanField,
} from 'react-admin';

interface Props {
  id?: any;
  record?: any;
  resource?: any;
}

const PostPanel: FC<Props> = ({ id, record, resource }) => (
  <div dangerouslySetInnerHTML={{ __html: record.object }} />
);

export const CovenantList: FC = (props) => (
  <List {...props} title="Listar convênios">
    <Datagrid expand={<PostPanel />}>
      <ImageField title="Logo" source="logo_file" />
      <TextField label="Nome convênio" source="name" />
      <TextField label="Iniciais" source="initials" />
      <BooleanField label="Finalizado?" source="finished" />
      <EditButton />
    </Datagrid>
  </List>
);
