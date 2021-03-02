// in src/users.js
import React, { FC } from 'react';
import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const StudentAdvisorList: FC = (props) => (
  <List {...props} title="Listar orientadores">
    <Datagrid>
      <TextField label="Matricula orientando" source="registration" />
      <TextField label="Nome orientador" source="advisor_name" />
      <EditButton />
    </Datagrid>
  </List>
);
