import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  SelectInput,
  ReferenceInput,
} from 'react-admin';

export const ProjectMemberEdit: FC = (props) => (
  <Edit {...props} title="Editar membro de projeto">
    <SimpleForm>
      <TextInput label="Nome" source="name" />
      <TextInput label="Cargo" source="job_title" />
      <ReferenceInput source="project" reference="projeto">
        <SelectInput optionText="name" />
      </ReferenceInput>
    </SimpleForm>
  </Edit>
);
