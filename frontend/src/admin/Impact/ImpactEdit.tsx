import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput } from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

export const ImpactEdit: FC = (props) => (
  <Edit {...props} title="Editar impacto">
    <SimpleForm>
      <TextInput disabled source="id" />
      <RichTextInput label="Texto" source="body" />
    </SimpleForm>
  </Edit>
);
