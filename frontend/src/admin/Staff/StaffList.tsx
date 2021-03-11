// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  ImageField,
  SelectField,
} from 'react-admin';

export const StaffList: FC = (props) => (
  <List {...props} title="Listar convênios">
    <Datagrid>
      <ImageField label="Foto" source="photo" />
      <TextField label="Nome membro" source="name" />
      <TextField label="Descrição" source="description" />
      <SelectField
        label="Tipo de membro"
        source="rank"
        choices={[
          { id: 'coordinator', name: 'Coordenador' },
          { id: 'vice_coordinator', name: 'Vice-Coordenador' },
          { id: 'secretariat', name: 'Secretário' },
          { id: 'intern', name: 'Bolsista' },
        ]}
      />
      <EditButton />
    </Datagrid>
  </List>
);
