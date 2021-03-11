import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput } from 'react-admin';

export const CovenantEdit: FC = (props) => (
  <Edit {...props} title="Editar convênio">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Nome" source="name" />
      <TextInput label="Iniciais" source="initials" />
    </SimpleForm>
  </Edit>
);
