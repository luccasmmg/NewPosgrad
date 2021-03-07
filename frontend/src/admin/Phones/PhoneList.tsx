// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  SelectField,
  EditButton,
} from 'react-admin';

export const PhoneList: FC = (props) => (
  <List {...props} title="Listar telefones">
    <Datagrid>
      <TextField source="id" />
      <SelectField
        label="Tipo"
        source="phone_type"
        choices={[
          { id: 'cellphone', name: 'Celular' },
          { id: 'fixed', name: 'Fixo' },
        ]}
      />
      <TextField label="Número" source="number" />
      <EditButton />
    </Datagrid>
  </List>
);
