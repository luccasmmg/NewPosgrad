import React, { FC } from 'react';
import { Create, SimpleForm, TextInput, SelectInput } from 'react-admin';

export const PhoneCreate: FC = (props) => (
  <Create {...props} title="Criar telefone">
    <SimpleForm>
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
  </Create>
);
