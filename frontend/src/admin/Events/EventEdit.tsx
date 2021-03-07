import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, DateTimeInput } from 'react-admin';

export const EventEdit: FC = (props) => (
  <Edit {...props} title="Editar evento">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Titulo" source="title" />
      <TextInput label="Link" source="link" />
      <DateTimeInput
        parse={(v: any) => v}
        label="Data inicial"
        source="initial_date"
      />
      <DateTimeInput
        parse={(v: any) => v}
        label="Data final"
        source="final_date"
      />
    </SimpleForm>
  </Edit>
);
