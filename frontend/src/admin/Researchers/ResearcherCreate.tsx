import React, { FC } from 'react';
import { Create, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const ResearcherCreate: FC = (props) => (
  <Create {...props} title="Criar Curso">
    <SimpleForm>
      <NumberInput label="CPF" source="cpf" />
      <TextInput label="Nome" source="name" />
    </SimpleForm>
  </Create>
);
