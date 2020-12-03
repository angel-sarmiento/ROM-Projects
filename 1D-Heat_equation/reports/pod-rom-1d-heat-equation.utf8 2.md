---
title: "Model Order Reduction of the 1-Dimensional Heat Equation "
author: "Angel Sarmiento - asarmiento6426@floridapoly.edu"
date: "12/2/2020"
output: 
  html_document
---





<img src="../python/images/models.gif" width="50%" height="50%" style="display: block; margin: auto;" />

<img src="../python/images/mu_plot_1.gif" width="32%" height="45%" /><img src="../python/images/mu_plot_2.gif" width="32%" height="45%" /><img src="../python/images/mu_plot_3.gif" width="32%" height="45%" />

<img src="../python/images/pod_bar.png" width="60%" height="60%" style="display: block; margin: auto;" />

<table class=" lightable-classic2" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> model </th>
   <th style="text-align:right;"> n_dim </th>
   <th style="text-align:right;"> RMSE </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> FOM </td>
   <td style="text-align:right;"> 128 </td>
   <td style="text-align:right;"> 0.0000000 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> ROM </td>
   <td style="text-align:right;"> 4 </td>
   <td style="text-align:right;"> 0.0259282 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> ROM_2 </td>
   <td style="text-align:right;"> 5 </td>
   <td style="text-align:right;"> 0.0125941 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> ROM_3 </td>
   <td style="text-align:right;"> 6 </td>
   <td style="text-align:right;"> 0.0079325 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> ROM_4 </td>
   <td style="text-align:right;"> 7 </td>
   <td style="text-align:right;"> 0.0061479 </td>
  </tr>
</tbody>
</table>


<img src="../python/images/pod_b1.gif" width="50%" height="50%" /><img src="../python/images/pod_b2.gif" width="50%" height="50%" /><img src="../python/images/pod_b3.gif" width="50%" height="50%" /><img src="../python/images/pod_b4.gif" width="50%" height="50%" />

