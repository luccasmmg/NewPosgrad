import React, { FC } from 'react';
import {
  Create,
  DateTimeInput,
  SimpleForm,
  TextInput,
  SelectInput,
} from 'react-admin';

export const ScheduledReportCreate: FC = (props) => (
  <Create {...props} title="Criar defesa">
    <SimpleForm>
      <TextInput label="Titulo" source="title" />
      <TextInput label="Autor" source="author" />
      <TextInput label="Localização" source="location" />
      <DateTimeInput
        label="Data - Horário"
        source="datetime"
        parse={(v: any) => v}
      />
    </SimpleForm>
  </Create>
);
