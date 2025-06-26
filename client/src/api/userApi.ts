import API from './http';
import type { User } from '../interfaces/User';

export const fetchUser = (userId: string) => API.get<User>(`/users/${userId}`);
export const fetchAllUsers = () => API.get<User[]>('/users');
export const createUserApi = (userData: Omit<User, 'id'>) => API.post<User>('/users', userData);
export const updateUserApi = (userId: string, userData: Partial<User>) => API.put<User>(`/users/${userId}`, userData);
export const deleteUserApi = (userId: string) => API.delete(`/users/${userId}`);