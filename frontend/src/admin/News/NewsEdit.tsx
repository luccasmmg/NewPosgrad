import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, DateInput } from 'react-admin';
import { RichTextField } from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

export const NewsEdit: FC = (props) => (
  <Edit {...props} title="Editar notícia">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Titulo" source="title" />
      <TextInput label="Subtítulo" source="headline" />
      <DateInput label="Data" source="date" />
      <RichTextInput label="Texto" source="body" />
    </SimpleForm>
  </Edit>
);
