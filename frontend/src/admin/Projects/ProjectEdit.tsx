import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  SelectInput,
  ReferenceInput,
} from 'react-admin';

export const ProjectEdit: FC = (props) => (
  <Edit {...props} title="Editar projeto">
    <SimpleForm>
      <TextInput label="Nome" source="name" />
      <TextInput label="Ano" source="year" />
      <TextInput label="Email" source="email" />
      <TextInput label="Situação" source="status" />
      <ReferenceInput source="coordinator" reference="pesquisador">
        <SelectInput optionText="name" />
      </ReferenceInput>
    </SimpleForm>
  </Edit>
);
