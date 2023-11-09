import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';

export const fetchAllSliders = createAsyncThunk(
  'slider/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      const response = await myApi.get('/sliders');
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const createSlider = createAsyncThunk(
  'slider/create',
  async (sliderData, { getState, rejectWithValue }) => {
    try {
      const token = getState().loginReducer.token;
      const response = await myApi.post('/sliders/create', sliderData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const updateSlider = createAsyncThunk(
  'slider/update',
  async ({ id, sliderData }, { getState, rejectWithValue }) => {
    try {
      const token = getState().loginReducer.token;
      const response = await myApi.put(`/sliders/update/${id}`, sliderData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const deleteSlider = createAsyncThunk(
  'slider/delete',
  async ({ id }, { getState, rejectWithValue }) => {
    try {
      const token = getState().loginReducer.token;
      const response = await myApi.delete(`/sliders/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const sliderSlice = createSlice({
  name: 'slider',
  initialState: {
    sliders: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllSliders.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllSliders.fulfilled, (state, action) => {
        state.loading = false;
        state.sliders = action.payload;
      })
      .addCase(fetchAllSliders.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(createSlider.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(createSlider.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(updateSlider.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(updateSlider.fulfilled, (state, action) => {
        state.loading = false;
        const updatedSlider = action.payload;
        const index = state.sliders.findIndex(
          (slider) => slider.slider_id === updatedSlider.id
        );
        if (index !== -1) {
          state.sliders[index] = updatedSlider;
        }
      })
      .addCase(updateSlider.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(deleteSlider.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(deleteSlider.fulfilled, (state, action) => {
        state.loading = false;
        const deletedSliderId = action.payload;
        state.sliders = state.sliders.filter(
          (slider) => slider.slider_id !== deletedSliderId
        );
      })
      .addCase(deleteSlider.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default sliderSlice.reducer;
