import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  SelectInput,
  ReferenceInput,
} from 'react-admin';

export const ProjectMemberCreate: FC = (props) => (
  <Create {...props} title="Adicionar membro a projeto">
    <SimpleForm>
      <TextInput label="Nome" source="name" />
      <TextInput label="Cargo" source="job_title" />
      <ReferenceInput source="project" reference="projeto">
        <SelectInput optionText="name" />
      </ReferenceInput>
    </SimpleForm>
  </Create>
);
