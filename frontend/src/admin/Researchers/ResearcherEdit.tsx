import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const ResearcherEdit: FC = (props) => (
  <Edit {...props} title="Editar Pesquisador">
    <SimpleForm>
      <NumberInput label="CPF" source="cpf" />
      <TextInput label="Nome" source="name" />
    </SimpleForm>
  </Edit>
);
