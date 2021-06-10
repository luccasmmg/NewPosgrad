import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  SelectInput,
  ReferenceInput,
} from 'react-admin';

export const ProjectCreate: FC = (props) => (
  <Create {...props} title="Criar projeto">
    <SimpleForm>
      <TextInput label="Nome" source="name" />
      <TextInput label="Ano" source="year" />
      <TextInput label="Email" source="email" />
      <TextInput label="Situação" source="status" />
      <ReferenceInput source="coordinator" reference="pesquisador">
        <SelectInput optionText="name" />
      </ReferenceInput>
    </SimpleForm>
  </Create>
);
