import React, { FC } from 'react';
import { Create, SimpleForm } from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

export const ImpactCreate: FC = (props) => (
  <Create {...props} title="Criar impacto">
    <SimpleForm>
      <RichTextInput label="Texto" source="body" />
    </SimpleForm>
  </Create>
);
