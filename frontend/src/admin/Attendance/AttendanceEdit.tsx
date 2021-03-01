import React, { FC } from 'react';
import { TopToolbar, Toolbar, SaveButton, Edit, SimpleForm, ListButton, TextInput, NumberInput } from 'react-admin';
import ChevronLeft from '@material-ui/icons/ChevronLeft';

const CustomToolbar: FC = props => (
	<Toolbar {...props}>
        <SaveButton />
    </Toolbar>
)

const CustomEditActions: any = ({ basePath }: any) => (
	<TopToolbar>
		<ListButton basePath={basePath} label="Voltar" icon={<ChevronLeft />} />
	</TopToolbar>
);

export const AttendanceEdit: FC = (props) => (
  <Edit {...props} actions={<CustomEditActions />} title="Editar Contato">
    <SimpleForm toolbar={<CustomToolbar />}>
      <TextInput type="email" label="Email" source="email" />
      <TextInput label="Localização" source="location" />
      <TextInput label="Horários" source="schedule" />
    </SimpleForm>
  </Edit>
);
