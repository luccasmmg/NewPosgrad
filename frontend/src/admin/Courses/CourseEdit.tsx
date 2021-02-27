import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const CourseEdit: FC = (props) => (
  <Edit {...props} title="Editar Curso">
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
  </Edit>
);
