import { fetchUtils } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import FormData from 'form-data';

const apiUrl = '/api/v1';

const httpClient = (url, options = {}) => {
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider(apiUrl, httpClient);

const myDataProvider = {
  ...dataProvider,
  create: (resource, params) => {
    if (!['convenio', 'documento', 'equipe'].includes(resource)) {
      return dataProvider.create(resource, params);
    }

    const reducer = (accumulator, currentValue) => {
      ['logo_file', 'file', 'photo'].includes(currentValue[0])
        ? accumulator.append(currentValue[0], currentValue[1].rawFile)
        : accumulator.append(currentValue[0], currentValue[1]);
      return accumulator;
    };

    return httpClient(`${apiUrl}/${resource}`, {
      method: 'POST',
      body: Object.entries(params.data).reduce(reducer, new FormData()),
    }).then(({ json }) => ({
      data: { ...params.data, id: json.id },
    }));
  },
};

export default myDataProvider;
