%%
% https://bispl.weebly.com/bispl-news/deep-learning-reconstruction-from-9-view-dual-energy-ct-for-baggage-inspection

%%
sz = [256, 256, 68];
header = 28;

name_data = 'Skull.vol';

fid = fopen(name_data, 'rb');
data = single(fread(fid, 'uint8'));
fclose(fid);
data = data((header+1):end);

data = reshape(data, sz);
data = permute(data, [3, 2, 1]);
data = flip(data, 1);
    
spacing = [4, 1, 1];
origin = [0, 0, 0];

vtkwrite('Skull_matlab.vtk', 'structured_points', 'Skull_matlab', data, ...
         'spacing', spacing(1), spacing(2), spacing(3), 'origin', origin(1), origin(2), origin(3));

%%
figure(1);
colormap gray;

subplot(131); 
imagesc(squeeze(data(35, :, :)));
axis image;
title('XY-axis');

subplot(132); 
imagesc(squeeze(data(:, 129, :)));
axis image;
title('XZ-axis');

subplot(133); 
imagesc(squeeze(data(:, :, 129)));
axis image;
title('YZ-axis');


%%
sz = [256, 256, 384];
header = 0;

name_data = 'proposed_256_256_384.raw';

fid = fopen(name_data, 'rb');
data = single(fread(fid, 'float32'));
fclose(fid);
data = data((header+1):end);

data = reshape(data, sz);
data = permute(data, [3, 2, 1]);
% data = flip(data, 1);
    
spacing = [1, 1, 1];
origin = [0, 0, 0];

vtkwrite('proposed_matlab.vtk', 'structured_points', 'proposed_matlab', data, ...
         'spacing', spacing(1), spacing(2), spacing(3), 'origin', origin(1), origin(2), origin(3));

%%
figure(2);
colormap gray;

subplot(131); 
imagesc(squeeze(data(floor(sz(3)/2), :, :)));
axis image;
title('XY-axis');

subplot(132); 
imagesc(squeeze(data(:, floor(sz(2)/2), :)));
axis image;
title('XZ-axis');

subplot(133); 
imagesc(squeeze(data(:, :, floor(sz(1)/2))));
axis image;
title('YZ-axis');

%%
sz = [256, 256, 384];
header = 0;

name_data = 'fbp_256_256_384.raw';

fid = fopen(name_data, 'rb');
data = single(fread(fid, 'float32'));
fclose(fid);
data = data((header+1):end);

data = reshape(data, sz);
data = permute(data, [3, 2, 1]);
% data = flip(data, 1);
    
spacing = [1, 1, 1];
origin = [0, 0, 0];

vtkwrite('fbp_matlab.vtk', 'structured_points', 'fbp_matlab', data, ...
         'spacing', spacing(1), spacing(2), spacing(3), 'origin', origin(1), origin(2), origin(3));

%%
figure(3);
colormap gray;

subplot(131); 
imagesc(squeeze(data(floor(sz(3)/2), :, :)));
axis image;
title('XY-axis');

subplot(132); 
imagesc(squeeze(data(:, floor(sz(2)/2), :)));
axis image;
title('XZ-axis');

subplot(133); 
imagesc(squeeze(data(:, :, floor(sz(1)/2))));
axis image;
title('YZ-axis');
