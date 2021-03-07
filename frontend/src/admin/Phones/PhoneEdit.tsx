import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, SelectInput } from 'react-admin';

export const PhoneEdit: FC = (props) => (
  <Edit {...props} title="Editar telefone">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Número" source="number" />
      <SelectInput
        label="Tipo de Número"
        source="phone_type"
        choices={[
          { id: 'cellphone', name: 'Celular' },
          { id: 'fixed', name: 'Fixo' },
        ]}
      />
    </SimpleForm>
  </Edit>
);
