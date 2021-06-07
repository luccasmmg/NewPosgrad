import React, { FC } from 'react';
import { Create, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const RepositoryDocsCreate: FC = (props) => (
  <Create {...props} title="Criar documento">
    <SimpleForm>
      <TextInput label="Titulo" source="title" />
      <TextInput label="Autor" source="author" />
      <NumberInput label="Ano" source="year" />
      <TextInput label="Link" source="link" />
    </SimpleForm>
  </Create>
);
