import React, { FC } from 'react';
import {
  Create,
  DateInput,
  SimpleForm,
  TextInput,
  SelectInput,
} from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

export const NewsCreate: FC = (props) => (
  <Create {...props} title="Criar notícia">
    <SimpleForm>
      <TextInput label="Titulo" source="title" />
      <TextInput label="Subtítulo" source="headline" />
      <DateInput label="Data" source="date" />
      <RichTextInput label="Texto" source="body" />
    </SimpleForm>
  </Create>
);
