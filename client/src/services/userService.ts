import {
    fetchUser,
    fetchAllUsers,
    createUserApi,
    updateUserApi,
    deleteUserApi,
  } from '../api/userApi';

import type { User } from '../interfaces/User';

export const getUser = async (userId: string): Promise<User> => {
  try {
    const response = await fetchUser(userId);
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
};

export const getAllUsers = async (): Promise<User[]> => {
  try {
    const response = await fetchAllUsers();
    return response.data;
  } catch (error) {
    console.error('Error fetching all users:', error);
    throw error;
  }
};

export const createUser = async (userData: Omit<User, 'id'>): Promise<User> => {
  try {
    const response = await createUserApi(userData);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};

export const updateUser = async (userId: string, userData: Partial<User>): Promise<User> => {
  try {
    const response = await updateUserApi(userId, userData);
    return response.data;
  } catch (error) {
    console.error('Error updating user:', error);
    throw error;
  }
};

export const deleteUser = async (userId: string): Promise<void> => {
  try {
    await deleteUserApi(userId);
  } catch (error) {
    console.error('Error deleting user:', error);
    throw error;
  }
};
