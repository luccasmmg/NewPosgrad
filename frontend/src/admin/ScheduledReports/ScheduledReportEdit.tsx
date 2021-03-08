import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, DateTimeInput } from 'react-admin';

export const ScheduledReportEdit: FC = (props) => (
  <Edit {...props} title="Editar defesa">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Titulo" source="title" />
      <TextInput label="Autor" source="author" />
      <TextInput label="Localização" source="location" />
      <DateTimeInput
        parse={(v: any) => v}
        label="Data - Horário"
        source="datetime"
      />
    </SimpleForm>
  </Edit>
);
