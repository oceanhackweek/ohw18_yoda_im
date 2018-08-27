
% Setup the varibles you need
instrument = 'CE04OSBP-LJ01C-06-CTDBPO108';
%instrument = 'RS01SBPS-SF01A-2A-CTDPFA102';
token      = 'V75GXAXOL3M2QD';
username   = 'OOIAPI-JB05CTD1GFAGGC';
t_start    = '2017-08-1T00:00:00.000Z';
t_end      = '2017-08-30T00:00:00.000Z';


% Get it
data = get_ooi_data(username,token,instrument,t_start,t_end);


%% Parse it
ooi.t   = [data.time]/86400 + datenum(1900,01,01);
ooi.T   = [data.seawater_temperature];
ooi.S   = [data.practical_salinity];
ooi.O   = [data.dissolved_oxygen];
ooi.P   = [data.pressure];
ooi.rho = [data.density];



% Quality Control
ooi.S(ooi.S < 30) = NaN;
ooi.O(ooi.O > 350) = NaN;
ooi.rho(ooi.rho < 1029.4) = NaN;


% Setup Plot
close all;
pagePortrait(1,10); clf;

% Plot Temperature
subplot(411);
plot(ooi.t,ooi.T,'r');
ylabel('Temperature (°C)');
set(gca,'xlim',limits(ooi.t));
datetick('x','keeplimits');
grid on;

% Plot Salinity
subplot(412);
plot(ooi.t,ooi.S,'color',ltblue);
ylabel('Salinity (psu)');
set(gca,'xlim',limits(ooi.t));
datetick('x','keeplimits');
grid on;

% Plot Density
subplot(413);
plot(ooi.t,ooi.rho,'color',purple);
ylabel('Density (kg m^{-3})');
set(gca,'xlim',limits(ooi.t));
datetick('x','keeplimits');
grid on;

% Plot Oxygen
subplot(414);
plot(ooi.t,ooi.O,'color',orange);
ylabel('Oxygen (\mumol)');
set(gca,'xlim',limits(ooi.t));
datetick('x','keeplimits');
grid on;



% Full Title
tstr = sprintf('Parameters from %s on %s at %s\n',instrument(end-8:end),instrument(10:end-13),instrument(1:8));
mtit(tstr,'FontWeight','Bold');




