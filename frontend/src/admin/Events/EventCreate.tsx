import React, { FC } from 'react';
import {
  Create,
  DateTimeInput,
  SimpleForm,
  TextInput,
  SelectInput,
} from 'react-admin';

export const EventCreate: FC = (props) => (
  <Create {...props} title="Criar evento">
    <SimpleForm>
      <TextInput label="Titulo" source="title" />
      <TextInput label="Link" source="link" />
      <DateTimeInput
        label="Data inicial"
        source="initial_date"
        locales="en-GB"
        parse={(v: any) => v}
      />
      <DateTimeInput
        label="Data final"
        source="final_date"
        parse={(v: any) => v}
      />
    </SimpleForm>
  </Create>
);
