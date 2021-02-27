// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  EditButton,
} from 'react-admin';

export const PosGraduationList: FC = (props) => (
  <List {...props} title="Listar Pós Graduações">
    <Datagrid>
      <TextField source="id" />
      <TextField label="ID Unidade" source="id_unit" />
      <TextField label="Código no Sigaa" source="sigaa_code" />
      <TextField label="Iniciais" source="initials" />
      <TextField label="Nome" source="name" />
      <TextField label="Descrição grande" source="description_big" />
      <TextField label="Descrição pequena" source="description_small" />
      <BooleanField label="Cadastrado?" source="is_signed_in" />
      <EditButton />
    </Datagrid>
  </List>
);
