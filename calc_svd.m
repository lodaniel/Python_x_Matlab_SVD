% Author: Luciano de Oliveira Daniel
% https://sites.google.com/site/professorlucianodaniel

% Carrega matriz A.
load('calc_svd_01.mat')
% Carrega matriz u.
load('calc_svd_02.mat')
% Carrega vetor s.
load('calc_svd_03.mat')
% Carrega matriz vh.
load('calc_svd_04.mat')
tic
s_M = svd(A);
toc
s_P = s_P';
[svdMs,I]=sort(s_M);
[svdPs,J]=sort(s_P);
erro=abs((s_P(J)-s_M(I))./s_M(I))*100;
x=1:length(erro);
plota_erro(x,erro);