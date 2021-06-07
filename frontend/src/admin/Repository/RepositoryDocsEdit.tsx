import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const RepositoryDocsEdit: FC = (props) => (
  <Edit {...props} title="Editar documento de repositorio">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Titulo" source="title" />
      <TextInput label="Autor" source="author" />
      <NumberInput label="Ano" source="year" />
      <TextInput label="Link" source="link" />
    </SimpleForm>
  </Edit>
);
