import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '@/helpers/api';

export const fetchAllSliders = createAsyncThunk(
  'sliders/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      const response = await myApi.get('/sliders');
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const fetchSliderById = createAsyncThunk(
  'sliders/fetchById',
  async (id, { rejectWithValue }) => {
    try {
      const response = await myApi.get(`/sliders/${id}`);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const createSlider = createAsyncThunk(
  'sliders/create',
  async (formData, { rejectWithValue }) => {
    try {
      const response = await myApi.post('/sliders/create', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const updateSliderById = createAsyncThunk(
  'sliders/updateById',
  async ({ id, formData }, { rejectWithValue }) => {
    try {
      const response = await myApi.put(`/sliders/${id}`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const deleteSliderById = createAsyncThunk(
  'sliders/deleteById',
  async (id, { rejectWithValue, getState }) => {
    try {
      const { accessToken } = getState().loginReducer;
      const response = await myApi.delete(`/sliders/${id}`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return rejectWithValue('Slider tidak ada');
      } else if (error.response && error.response.status === 403) {
        return rejectWithValue(
          'Anda tidak memiliki izin untuk menghapus slider tersebut'
        );
      } else {
        return rejectWithValue('Gagal menghapus slider');
      }
    }
  }
);

const initialState = {
  slider: null,
  sliders: [],
  loading: false,
  error: null,
};

const slidersSlice = createSlice({
  name: 'sliders',
  initialState: initialState,
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
      .addCase(fetchSliderById.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchSliderById.fulfilled, (state, action) => {
        state.loading = false;
        state.slider = action.payload;
      })
      .addCase(fetchSliderById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(createSlider.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(createSlider.fulfilled, (state, action) => {
        state.loading = false;
        state.sliders.push(action.payload);
      })
      .addCase(createSlider.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(updateSliderById.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(updateSliderById.fulfilled, (state, action) => {
        state.loading = false;
        const sliderIndex = state.sliders.findIndex(
          (slider) => slider.slider_id === action.payload.id
        );
        if (sliderIndex !== -1) {
          state.sliders[sliderIndex] = action.payload;
        }
      })
      .addCase(updateSliderById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(deleteSliderById.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(deleteSliderById.fulfilled, (state, action) => {
        state.loading = false;
        state.sliders = state.sliders.filter(
          (slider) => slider.slider_id !== action.payload
        );
      })
      .addCase(deleteSliderById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default slidersSlice.reducer;
