// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  EditButton,
} from 'react-admin';

export const ParticipationList: FC = (props) => (
  <List {...props} title="Listar participações">
    <Datagrid>
      <TextField label="Título participação" source="title" />
      <TextField label="Descrição participação" source="description" />
      <TextField label="Ano participação" source="year" />
      <BooleanField
        label="Participação Internacional?"
        source="international"
      />
      <EditButton />
    </Datagrid>
  </List>
);
