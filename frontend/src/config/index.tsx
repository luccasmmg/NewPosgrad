const BASE_URL: string = process.env.NODE_ENV === 'production' ? 'http://localhost:8000' : '';
export default BASE_URL;
