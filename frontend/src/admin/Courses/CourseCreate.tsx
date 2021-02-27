import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  BooleanInput,
  NumberInput,
} from 'react-admin';

export const CourseCreate: FC = (props) => (
  <Create {...props} title="Criar Curso">
    <SimpleForm>
      <NumberInput label="ID da Pós" source="owner_id" />
      <NumberInput label="Id no Sigaa" source="id_sigaa" />
      <TextInput label="Nome" source="name" />
      <TextInput
        type="url"
        label="URL no Repositório Institucional"
        source="institutional_repository_url"
      />
      <TextInput label="Type de Curso" source="course_type" />
    </SimpleForm>
  </Create>
);
